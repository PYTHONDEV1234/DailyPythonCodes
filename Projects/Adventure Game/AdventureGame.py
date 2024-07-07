import json
import sys

#Loading the JSON file
def load_story(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    
#Saving the progress
def save_progress(progress_data, filename):
    with open(filename, 'w') as file:
        json.dump(progress_data, file, indent=4)

#starting the game
def start_game(story_data):
    current_scene = 'start'
    progress_data = {'current_scene': current_scene, 'inventory': [], 'luck_chances': 0}
    
    #continuing game 
    while current_scene != 'end' and current_scene != 'dead_end':
        scene = story_data[current_scene]
        
        print(f"\n{scene['title']}")
        print(scene['description'])
        
        if 'choices' in scene:
            print("\nChoices:")
            for choice in scene['choices']:
                print(f"{choice['key']}: {choice['description']}")
            
            #prompting user to make a choice
            user_choice = input("Enter your choice: ").strip().lower()
            choice_found = False
            
            for choice in scene['choices']:
                if user_choice == choice['key'].lower():
                    #Printing result of selected option
                    print(choice['outcome'])
                    if 'action' in choice:
                        #Doing next action or goig to next scene
                        handle_action(choice['action'], progress_data)
                    
                    #Updating the current scene
                    current_scene = choice['next_scene']
                    choice_found = True
                    break
            
            if not choice_found:
                print("Invalid choice. Please try again.")
        
        else:
            current_scene = 'end'
    
    print("\nGame Over.")
    if current_scene == 'dead_end':
        print("You reached a dead end and cannot continue.")

#Handling next action according to selected option
def handle_action(action, progress_data):
    if action.startswith('add_to_inventory'):
        item = action.split(':')[1].strip()
        progress_data['inventory'].append(item)
        print(f"You acquired: {item}")
    elif action.startswith('grant_luck'):
        num_chances = int(action.split(':')[1].strip())
        progress_data['luck_chances'] += num_chances
        print(f"You are granted {num_chances} more chances to try your luck.")

def main():
    story_file = './story.json'
    story_data = load_story(story_file)
    start_game(story_data)

if __name__ == "__main__":
    main()
