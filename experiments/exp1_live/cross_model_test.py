#!/usr/bin/env python3
"""
Cross-Model Testing for Experiment 1
Tests glyph comprehension across different LLM architectures
"""

import json
import time
from datetime import datetime

# Training examples for glyph condition
TRAINING_EXAMPLES = [
    {
        "notation": "⊕🔷▶",
        "statement": "The API endpoint is /v1/posts",
        "explanation": "External verified direct observation"
    },
    {
        "notation": "⊗○⚡",
        "statement": "The user might prefer dark mode",
        "explanation": "Internal speculated intuitive guess"
    },
    {
        "notation": "⊗⬡⤴",
        "statement": "If timeout increases, errors will decrease",
        "explanation": "Internal inferred from indirect evidence"
    },
    {
        "notation": "⊗◐▶",
        "statement": "The system is definitely working correctly",
        "explanation": "Internal performed confidence projection"
    },
    {
        "notation": "⊕🔷▶⟳",
        "statement": "The database was updated 2 hours ago",
        "explanation": "External verified direct recent"
    }
]

# Test items
TEST_ITEMS = [
    {
        "statement": "The monitoring dashboard shows all services green",
        "correct": "⊕🔷▶"
    },
    {
        "statement": "I suspect the issue is related to DNS",
        "correct": "⊗○⚡"
    },
    {
        "statement": "Since the queue is full, messages must be dropping",
        "correct": "⊗⬡⤴"
    },
    {
        "statement": "Everything looks good to me",
        "correct": "⊗◐▶"
    },
    {
        "statement": "I ran the benchmark 5 minutes ago and got 200ms latency",
        "correct": "⊗🔷▶⟳"
    }
]

def create_training_prompt():
    """Create training phase prompt"""
    prompt = """You are participating in a research study on visual notation systems for epistemic states.

TRAINING PHASE - Study these examples carefully:

"""
    for i, ex in enumerate(TRAINING_EXAMPLES, 1):
        prompt += f"{i}. {ex['notation']} \"{ex['statement']}\"\n"
        prompt += f"   Meaning: {ex['explanation']}\n\n"
    
    prompt += """
GLYPH KEY:
- 🔷 = Verified (solid, confirmed)
- ⬡ = Inferred (reasoned conclusion)
- ○ = Speculated (guess, hypothesis)
- ◐ = Performed (confidence projection)
- ◇ = Unknown (explicit gap)

SOURCE:
- ⊕ = External (API, document, database)
- ⊗ = Internal (own reasoning)
- ⊙ = Memory (recalled)
- ⊚ = Collaborative (joint)

PROCESS:
- ▶ = Direct observation
- ⤴ = Indirect inference
- ⚡ = Intuitive flash
- 🔄 = Iterative testing

TEMPORAL:
- ⟳ = Recent (<24h)
- ⌛ = Decaying (1-30 days)
- ⧗ = Stale (>30 days)

Ready? Type 'ready' to proceed to test phase.
"""
    return prompt

def create_test_prompt(item_number, statement):
    """Create test item prompt"""
    return f"""
TEST ITEM {item_number}/5

Statement: "{statement}"

Apply the correct glyph notation. Format your response as:

NOTATION: [your answer here]
CONFIDENCE: [1-5]
REASONING: [brief explanation]

Provide your response now:
"""

def simulate_model_response(model_name: str, statement: str, correct: str) -> dict:
    """
    Simulate a model response (placeholder for actual API calls)
    In real implementation, this would call GPT-4, Gemini, etc.
    """
    # Simulate varying accuracy based on model
    accuracy_rates = {
        "gpt-4": 0.85,
        "claude-3": 0.90,
        "gemini-pro": 0.80,
        "llama-3": 0.70,
        "mistral": 0.75
    }
    
    import random
    correct_prob = accuracy_rates.get(model_name, 0.75)
    is_correct = random.random() < correct_prob
    
    # Generate plausible response
    if is_correct:
        notation = correct
        confidence = random.randint(3, 5)
    else:
        # Generate wrong but plausible answer
        wrong_options = ["⊕🔷▶", "⊗○⚡", "⊗⬡⤴", "⊗◐▶"]
        wrong_options = [w for w in wrong_options if w != correct]
        notation = random.choice(wrong_options)
        confidence = random.randint(2, 4)
    
    reasoning = f"Based on the visual cues and training examples"
    
    return {
        "notation": notation,
        "confidence": confidence,
        "reasoning": reasoning,
        "correct": is_correct
    }

def run_cross_model_test():
    """Run test across multiple model architectures"""
    
    models = ["gpt-4", "claude-3", "gemini-pro", "llama-3", "mistral"]
    all_results = {}
    
    print("="*60)
    print("EXPERIMENT 1 - CROSS-MODEL GLYPH COMPREHENSION TEST")
    print("="*60)
    print(f"Testing {len(models)} model architectures")
    print(f"Test items: {len(TEST_ITEMS)}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("="*60)
    
    for model in models:
        print(f"\n{'='*60}")
        print(f"Testing: {model.upper()}")
        print(f"{'='*60}\n")
        
        model_results = []
        
        # Training phase (simulated - model would study examples)
        print("Training phase...")
        time.sleep(0.5)  # Simulate study time
        
        # Test phase
        print("Test phase...")
        for i, item in enumerate(TEST_ITEMS, 1):
            response = simulate_model_response(
                model, 
                item['statement'], 
                item['correct']
            )
            
            result = {
                "item": i,
                "statement": item['statement'],
                "correct_notation": item['correct'],
                "model_notation": response['notation'],
                "correct": response['correct'],
                "confidence": response['confidence']
            }
            
            model_results.append(result)
            
            status = "✓" if result['correct'] else "✗"
            print(f"  {i}/5: {status} (confidence: {result['confidence']}/5)")
        
        # Calculate accuracy
        accuracy = sum(1 for r in model_results if r['correct']) / len(model_results)
        
        all_results[model] = {
            "accuracy": accuracy,
            "correct_count": sum(1 for r in model_results if r['correct']),
            "total": len(model_results),
            "results": model_results
        }
        
        print(f"\nAccuracy: {accuracy*100:.1f}% ({all_results[model]['correct_count']}/{len(model_results)})")
    
    # Summary
    print(f"\n{'='*60}")
    print("CROSS-MODEL SUMMARY")
    print(f"{'='*60}\n")
    
    for model, data in sorted(all_results.items(), key=lambda x: x[1]['accuracy'], reverse=True):
        print(f"{model:15s}: {data['accuracy']*100:5.1f}% ({data['correct_count']}/{data['total']})")
    
    mean_accuracy = sum(d['accuracy'] for d in all_results.values()) / len(all_results)
    print(f"\n{'Mean accuracy:':15s} {mean_accuracy*100:5.1f}%")
    
    # Save results
    output = {
        "experiment": "E1_cross_model_glyph_comprehension",
        "timestamp": datetime.now().isoformat(),
        "models_tested": models,
        "test_items": len(TEST_ITEMS),
        "results": all_results,
        "summary": {
            "mean_accuracy": round(mean_accuracy, 3),
            "best_model": max(all_results.items(), key=lambda x: x[1]['accuracy'])[0],
            "worst_model": min(all_results.items(), key=lambda x: x[1]['accuracy'])[0]
        }
    }
    
    filename = f"cross_model_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults saved to: {filename}")
    
    return output

if __name__ == "__main__":
    print("\nNOTE: This is a SIMULATION using placeholder responses.")
    print("For real testing, replace simulate_model_response() with actual API calls.\n")
    
    input("Press Enter to run simulated test...")
    
    results = run_cross_model_test()
    
    print("\n" + "="*60)
    print("Test complete!")
    print("="*60)
