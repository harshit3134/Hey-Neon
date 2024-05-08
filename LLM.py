import webbrowser
import pyautogui
import subprocess
import json

def open_website(args):
    for url in args:
        webbrowser.open(url)
    return None


def simulate_key_press(*args):
    pyautogui.hotkey(*args)
    return None


def open_application(command):
    subprocess.Popen(command, shell=True)
    return None


def get_action(action):
  custom_functions = [
    {
      'name': 'open_website',
      'description': 'Open one or more websites in the default browser',
      'parameters': {
        'type': 'object', 
        'properties': {
          'urls': {
            'type': 'array',
            'items': {'type': 'string'},
            'description': 'List of website URLs to open'
          }  
        }
      }
    },
    {
      'name': 'simulate_key_press',
      'description': 'Simulate pressing keyboard shortcuts', 
      'parameters': {
        'type': 'object',
        'properties': {
          'keys': {
            'type': 'array',
            'items': {'type': 'string'},
            'description': 'Allows you to emulate key presses, such as reopening the last closed tab with Ctrl+Shift+T,Capture Screenshot Win+Shift+S, enabling the execution of specific commands typically performed through keyboard shortcuts. Before executing this event, you will ask for permission to use the command. The event uses common key names compatible with libraries like PyAutoGUI to accurately simulate key presses.' 
          }
        }
      }
    },
    { 
      'name': 'open_application',
      'description': 'Open Windows Application. This uses python subprocess library in backend with shell=True',
      'parameters': {
        'type': 'object',
        'properties': {
          'command': {
            'type': 'string',
            'description': 'Command to run to open application'
          }
        }
      }
    }
  ]

  import openai
  import json
  command=action

  response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role': 'user', 'content': command}],
        functions = custom_functions,
        function_call = 'auto'
)

  response_message = response.choices[0].message

  if dict(response_message).get('function_call'):
    function_called = response_message.function_call.name
    print("the function called is "+ function_called)
    function_args  = json.loads(response_message.function_call.arguments)
    print("the function args are "+ str(function_args))
    available_functions = {
            "open_website": open_website,
            "simulate_key_press": simulate_key_press,
            "open_application": open_application
  }
        
  fuction_to_call = available_functions[function_called]
  response_message = fuction_to_call(*list(function_args .values()))

  # else:
  #   response_message = response_message.content
  print(response_message)


if __name__ == "__main__":
    get_action("Open Windows Terminal")