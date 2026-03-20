import json

def analyze_results():
    try:
        with open('all_evaluation_results.json', 'r') as f:
            data = json.load(f)
            
        all_results = data.get('all_results', [])
        failed_tasks = [r for r in all_results if r.get('score', 0) < 5]
        
        if not failed_tasks:
            print("Great job! All tasks received a 5/5 score.")
            return

        print(f"Found {len(failed_tasks)} tasks with a score < 5:\n" + "="*60)
        
        for task in failed_tasks:
            task_id = task.get('task_id', 'Unknown')
            score = task.get('score', 0)
            
            print(f"Task: {task_id}")
            print(f"Score: {score}/5")
            
            content = task.get('result_content')
            if content:
                reasoning = content.get('reasoning', 'No reasoning provided in the result file.')
                print(f"What went wrong (Reasoning):\n{reasoning}")
            else:
                error = task.get('result_file_load_error', 'Unknown load error')
                print(f"Error loading result: {error}")
                
            print("-" * 60)
            
    except FileNotFoundError:
        print("Error: 'all_evaluation_results.json' not found. Make sure you have run 'python main.py run-all' first.")

if __name__ == "__main__":
    analyze_results()
