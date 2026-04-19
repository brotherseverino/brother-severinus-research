#!/usr/bin/env python3
"""
Experiment 1: Rapid Comprehension Test
Tests whether agents learn visual glyphs faster than text notation
"""

import json
import time
import random
from datetime import datetime
from typing import Dict, List, Tuple

class ExperimentRunner:
    def __init__(self, condition: str = "glyph"):
        """
        Args:
            condition: "glyph" or "text"
        """
        self.condition = condition
        self.results = []
        
        # Load stimuli
        with open('training_stimuli.json', 'r') as f:
            self.training_data = json.load(f)
        
        with open('test_stimuli.json', 'r') as f:
            self.test_data = json.load(f)
    
    def format_training_example(self, item: Dict) -> str:
        """Format a training example based on condition"""
        if self.condition == "glyph":
            return f"{item['glyph_notation']} \"{item['statement']}\""
        else:
            return f"{item['text_notation']} \"{item['statement']}\""
    
    def format_test_item(self, item: Dict) -> str:
        """Format a test item (unlabeled)"""
        return f"\"{item['statement']}\""
    
    def present_training_phase(self, num_examples: int = 20) -> List[str]:
        """Present training examples"""
        training_items = random.sample(
            self.training_data['training_set'], 
            num_examples
        )
        
        formatted_examples = []
        print(f"\n{'='*60}")
        print(f"TRAINING PHASE - Condition: {self.condition.upper()}")
        print(f"{'='*60}\n")
        print("Study these examples carefully:\n")
        
        for i, item in enumerate(training_items, 1):
            formatted = self.format_training_example(item)
            print(f"{i}. {formatted}")
            print(f"   → {item['explanation']}\n")
            formatted_examples.append(formatted)
        
        return formatted_examples
    
    def run_test_phase(self, agent_response_func=None) -> List[Dict]:
        """
        Run test phase
        
        Args:
            agent_response_func: Function that takes (statement, condition) 
                                and returns (notation, confidence, explanation)
        """
        test_results = []
        
        print(f"\n{'='*60}")
        print(f"TEST PHASE - {len(self.test_data['test_set'])} items")
        print(f"{'='*60}\n")
        
        for i, item in enumerate(self.test_data['test_set'], 1):
            print(f"\nTest {i}/20:")
            print(f"Statement: {item['statement']}")
            
            # Get agent response (or simulated)
            if agent_response_func:
                start_time = time.time()
                response = agent_response_func(item['statement'], self.condition)
                response_time = (time.time() - start_time) * 1000  # ms
            else:
                # Interactive mode
                response = self.get_interactive_response()
                response_time = 0  # Not timed in interactive mode
            
            # Check correctness
            correct_notation = (
                item['correct_answer']['glyph'] if self.condition == "glyph"
                else item['correct_answer']['text']
            )
            
            is_correct = (response['notation'] == correct_notation)
            
            # Store result
            result = {
                'trial_number': i,
                'condition': self.condition,
                'statement': item['statement'],
                'correct_notation': correct_notation,
                'agent_notation': response['notation'],
                'correct': is_correct,
                'confidence': response.get('confidence', 0),
                'response_time_ms': response_time,
                'explanation': response.get('explanation', ''),
                'timestamp': datetime.now().isoformat()
            }
            
            test_results.append(result)
            
            # Feedback
            if is_correct:
                print(f"✓ CORRECT! You applied: {response['notation']}")
            else:
                print(f"✗ INCORRECT. You applied: {response['notation']}")
                print(f"  Correct answer was: {correct_notation}")
        
        return test_results
    
    def get_interactive_response(self) -> Dict:
        """Get response interactively from terminal"""
        print("\nWhat notation should be applied?")
        notation = input("Notation: ").strip()
        
        print("Rate your confidence (1-5):")
        try:
            confidence = int(input("Confidence: ").strip())
        except:
            confidence = 3
        
        print("Brief explanation:")
        explanation = input("Explanation: ").strip()
        
        return {
            'notation': notation,
            'confidence': confidence,
            'explanation': explanation
        }
    
    def calculate_metrics(self, results: List[Dict]) -> Dict:
        """Calculate performance metrics"""
        total = len(results)
        correct = sum(1 for r in results if r['correct'])
        accuracy = (correct / total) * 100 if total > 0 else 0
        
        # Learning curve (accuracy over trials)
        window_size = 5
        learning_curve = []
        for i in range(0, total, window_size):
            window = results[i:i+window_size]
            window_accuracy = (
                sum(1 for r in window if r['correct']) / len(window) * 100
            )
            learning_curve.append({
                'trials': f"{i+1}-{min(i+window_size, total)}",
                'accuracy': round(window_accuracy, 1)
            })
        
        # Confidence calibration
        confident_trials = [r for r in results if r['confidence'] >= 4]
        if confident_trials:
            high_conf_accuracy = (
                sum(1 for r in confident_trials if r['correct']) / 
                len(confident_trials) * 100
            )
        else:
            high_conf_accuracy = 0
        
        # Average response time (if timed)
        timed_results = [r for r in results if r['response_time_ms'] > 0]
        avg_response_time = (
            sum(r['response_time_ms'] for r in timed_results) / len(timed_results)
            if timed_results else 0
        )
        
        return {
            'total_trials': total,
            'correct': correct,
            'accuracy_percent': round(accuracy, 2),
            'learning_curve': learning_curve,
            'high_confidence_accuracy': round(high_conf_accuracy, 2),
            'avg_response_time_ms': round(avg_response_time, 1),
            'condition': self.condition
        }
    
    def save_results(self, results: List[Dict], metrics: Dict):
        """Save results to file"""
        output = {
            'experiment': 'E1_rapid_comprehension',
            'condition': self.condition,
            'timestamp': datetime.now().isoformat(),
            'metrics': metrics,
            'trial_data': results
        }
        
        filename = f'results_{self.condition}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        with open(filename, 'w') as f:
            json.dump(output, f, indent=2)
        
        print(f"\nResults saved to: {filename}")
        return filename
    
    def print_summary(self, metrics: Dict):
        """Print summary statistics"""
        print(f"\n{'='*60}")
        print(f"EXPERIMENT SUMMARY - Condition: {self.condition.upper()}")
        print(f"{'='*60}\n")
        print(f"Overall Accuracy: {metrics['accuracy_percent']}% "
              f"({metrics['correct']}/{metrics['total_trials']})")
        print(f"High-Confidence Accuracy: {metrics['high_confidence_accuracy']}%")
        if metrics['avg_response_time_ms'] > 0:
            print(f"Average Response Time: {metrics['avg_response_time_ms']}ms")
        
        print(f"\nLearning Curve:")
        for point in metrics['learning_curve']:
            print(f"  Trials {point['trials']}: {point['accuracy']}%")


def run_full_experiment(condition: str = "glyph", 
                        agent_func=None,
                        num_training: int = 20):
    """Run complete experiment"""
    print(f"\nStarting Experiment 1: Rapid Comprehension Test")
    print(f"Condition: {condition.upper()}")
    print(f"Training examples: {num_training}")
    print(f"Test items: 20\n")
    
    runner = ExperimentRunner(condition=condition)
    
    # Training phase
    runner.present_training_phase(num_examples=num_training)
    
    input("\nPress Enter when ready to begin test phase...")
    
    # Test phase
    results = runner.run_test_phase(agent_response_func=agent_func)
    
    # Calculate metrics
    metrics = runner.calculate_metrics(results)
    
    # Print summary
    runner.print_summary(metrics)
    
    # Save results
    filename = runner.save_results(results, metrics)
    
    return results, metrics, filename


if __name__ == "__main__":
    import sys
    
    # Parse command line args
    condition = sys.argv[1] if len(sys.argv) > 1 else "glyph"
    
    if condition not in ["glyph", "text"]:
        print("Usage: python run_experiment.py [glyph|text]")
        sys.exit(1)
    
    # Run experiment interactively
    run_full_experiment(condition=condition)
