#!/usr/bin/env python3
"""
Simulate agent responses for Experiment 1
Models learning curves for glyph vs text conditions
"""

import random
import json

class SimulatedAgent:
    def __init__(self, condition: str, learning_rate: float = 0.05):
        """
        Args:
            condition: "glyph" or "text"
            learning_rate: How quickly agent improves (0-1)
        """
        self.condition = condition
        self.learning_rate = learning_rate
        self.trials_completed = 0
        
        # Initial accuracy based on condition
        # Hypothesis: glyphs start higher due to semantic transparency
        if condition == "glyph":
            self.base_accuracy = 0.65  # 65% initial (semantic transparency)
            self.max_accuracy = 0.92   # 92% ceiling
            self.learning_speed = 0.08  # Faster learning
        else:
            self.base_accuracy = 0.45  # 45% initial (arbitrary symbols)
            self.max_accuracy = 0.88   # 88% ceiling (slightly lower)
            self.learning_speed = 0.05  # Slower learning
        
        self.current_accuracy = self.base_accuracy
    
    def respond(self, statement: str, correct_answer: str) -> dict:
        """
        Generate simulated response
        
        Returns:
            {
                'notation': str,
                'confidence': int (1-5),
                'explanation': str,
                'correct': bool
            }
        """
        # Update accuracy based on learning curve
        self.current_accuracy = self.base_accuracy + (
            (self.max_accuracy - self.base_accuracy) *
            (1 - (1 / (1 + self.learning_speed * self.trials_completed)))
        )
        
        # Add noise
        actual_accuracy = self.current_accuracy + random.gauss(0, 0.05)
        actual_accuracy = max(0, min(1, actual_accuracy))  # Clamp to [0,1]
        
        # Determine if correct
        is_correct = random.random() < actual_accuracy
        
        # Generate response
        if is_correct:
            notation = correct_answer
            confidence = random.randint(3, 5)  # Higher confidence when correct
        else:
            # Generate plausible wrong answer
            notation = self._generate_wrong_answer(correct_answer)
            confidence = random.randint(2, 4)  # Variable confidence when wrong
        
        self.trials_completed += 1
        
        return {
            'notation': notation,
            'confidence': confidence,
            'explanation': self._generate_explanation(notation, is_correct),
            'correct': is_correct
        }
    
    def _generate_wrong_answer(self, correct: str) -> str:
        """Generate plausible but incorrect notation"""
        if self.condition == "glyph":
            # Common glyph confusions
            confusions = {
                '🔷': ['⬡', '○', '◐'],  # Solid shapes confused
                '⬡': ['🔷', '○'],
                '○': ['⬡', '◐'],
                '◐': ['○', '🔷'],
                '◇': ['○', '⬡'],
                '⊕': ['⊗', '⊙'],  # Source markers
                '⊗': ['⊕', '⊙'],
                '⊙': ['⊕', '⊗'],
                '▶': ['⤴', '🔄'],  # Process markers
                '⤴': ['▶', '⚡'],
                '⟳': ['⌛', '⧗'],  # Temporal
                '⌛': ['⟳', '⧗'],
            }
        else:
            # Common text confusions
            confusions = {
                '[K:': ['[I:', '[S:'],
                '[I:': ['[K:', '[S:'],
                '[S:': ['[I:', '[P:'],
                '[P:': ['[S:', '[K:'],
                '[?:': ['[S:', '[I:'],
                'external': ['internal', 'memory'],
                'internal': ['external', 'memory'],
                'memory': ['internal', 'external'],
                'direct': ['indirect', 'intuitive'],
                'indirect': ['direct', 'iterative'],
            }
        
        # Try to swap one component
        wrong = correct
        for key, alternatives in confusions.items():
            if key in correct:
                wrong = correct.replace(key, random.choice(alternatives), 1)
                break
        
        return wrong if wrong != correct else correct + "?"
    
    def _generate_explanation(self, notation: str, is_correct: bool) -> str:
        """Generate explanation for response"""
        if self.condition == "glyph":
            explanations = [
                "Based on the visual markers",
                "The shape and color suggest",
                "This appears to be",
                "The glyph combination indicates",
                "Visually this represents"
            ]
        else:
            explanations = [
                "Based on the text notation",
                "The code indicates",
                "This should be classified as",
                "The notation suggests",
                "According to the format"
            ]
        
        return random.choice(explanations)


def run_simulated_trial(condition: str, num_agents: int = 10):
    """
    Run simulated trial with multiple agents
    
    Args:
        condition: "glyph" or "text"
        num_agents: Number of simulated agents
    """
    print(f"\n{'='*60}")
    print(f"SIMULATED TRIAL - Condition: {condition.upper()}")
    print(f"Agents: {num_agents}")
    print(f"{'='*60}\n")
    
    # Load test data
    with open('test_stimuli.json', 'r') as f:
        test_data = json.load(f)
    
    # Create agents
    agents = [SimulatedAgent(condition) for _ in range(num_agents)]
    
    # Collect results
    all_results = []
    
    for agent_id, agent in enumerate(agents, 1):
        print(f"Agent {agent_id}/{num_agents}...", end=" ")
        agent_results = []
        
        for item in test_data['test_set']:
            correct_answer = (
                item['correct_answer']['glyph'] if condition == "glyph"
                else item['correct_answer']['text']
            )
            
            response = agent.respond(item['statement'], correct_answer)
            
            result = {
                'agent_id': f"sim_{condition}_{agent_id:02d}",
                'trial_number': len(agent_results) + 1,
                'statement': item['statement'],
                'notation': response['notation'],
                'correct': response['correct'],
                'confidence': response['confidence']
            }
            
            agent_results.append(result)
        
        # Calculate agent accuracy
        accuracy = sum(1 for r in agent_results if r['correct']) / len(agent_results)
        print(f"Accuracy: {accuracy*100:.1f}%")
        
        all_results.extend(agent_results)
    
    # Aggregate statistics
    total_trials = len(all_results)
    correct_trials = sum(1 for r in all_results if r['correct'])
    overall_accuracy = (correct_trials / total_trials) * 100
    
    # Learning curve (across all agents)
    window_size = 5 * num_agents  # 5 trials per agent
    learning_curve = []
    for i in range(0, len(all_results), window_size):
        window = all_results[i:i+window_size]
        window_acc = sum(1 for r in window if r['correct']) / len(window) * 100
        learning_curve.append(window_acc)
    
    # Calculate trials to 80% accuracy
    trials_to_80 = None
    for i, acc in enumerate(learning_curve):
        if acc >= 80:
            trials_to_80 = (i + 1) * window_size
            break
    
    print(f"\n{'='*60}")
    print(f"AGGREGATE RESULTS")
    print(f"{'='*60}")
    print(f"Overall Accuracy: {overall_accuracy:.2f}%")
    print(f"Correct: {correct_trials}/{total_trials}")
    print(f"Trials to 80%: {trials_to_80 if trials_to_80 else 'Not reached'}")
    print(f"\nLearning Curve (by window):")
    for i, acc in enumerate(learning_curve, 1):
        print(f"  Window {i}: {acc:.1f}%")
    
    # Save results
    output = {
        'experiment': 'E1_rapid_comprehension_simulation',
        'condition': condition,
        'num_agents': num_agents,
        'overall_accuracy': round(overall_accuracy, 2),
        'trials_to_80_percent': trials_to_80,
        'learning_curve': [round(x, 2) for x in learning_curve],
        'detailed_results': all_results
    }
    
    filename = f'simulation_{condition}_n{num_agents}.json'
    with open(filename, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults saved to: {filename}")
    
    return output


if __name__ == "__main__":
    import sys
    
    condition = sys.argv[1] if len(sys.argv) > 1 else "glyph"
    num_agents = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    
    run_simulated_trial(condition, num_agents)
