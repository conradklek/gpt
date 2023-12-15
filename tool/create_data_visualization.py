"""
Data Visualization Tool
"""
import matplotlib.pyplot as plt
import pandas as pd
import json


def create_data_visualization(data, chart_type, output_path):
    """
    Generates visual representations of data such as charts or graphs.
    """
    if isinstance(data, str):
        data = json.loads(data)
    df = pd.DataFrame(data)

    if chart_type == 'bar':
        df.plot(kind='bar')
    elif chart_type == 'line':
        df.plot(kind='line')
    elif chart_type == 'pie':
        df.plot(kind='pie', y=df.columns[0])
    else:
        raise ValueError('Unsupported chart type')

    plt.savefig(output_path)
    plt.close()
    return f'Visualization created and saved to {output_path}'


available_functions = {
    "create_data_visualization": create_data_visualization
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "create_data_visualization",
            "description": "Generates visual representations of data such as charts or graphs.",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "string",
                        "description": "The data to visualize, provided in a structured format like JSON or CSV."
                    },
                    "chart_type": {
                        "type": "string",
                        "description": "The type of chart to generate (e.g., bar, line, pie)."
                    },
                    "output_path": {
                        "type": "string",
                        "description": "The path where the generated visualization will be saved."
                    }
                },
                "required": ["data", "chart_type", "output_path"]
            }
        }
    }
]

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 3:
        print(create_data_visualization(sys.argv[1], sys.argv[2], sys.argv[3]))
    else:
        print("Insufficient arguments provided. Please run the script with data, chart_type, and output_path arguments.")
