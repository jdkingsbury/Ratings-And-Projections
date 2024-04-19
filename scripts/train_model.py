import os
from ludwig.api import LudwigModel
from ludwig.utils.data_utils import load_csv

def train_model(config_path, dataset_path, output_directory):

    # Load config
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Load dataset
    dataset = load_csv(dataset_path)

    # Train model
    train_stats = model.train(dataset=dataset, output_directory=output_directory)

    # Output training stats
    print(train_stats)

    # Save model
    model_path = os.path.join(output_directory, 'model')
    model.save(model_path)

    # Close model
    model.close()

    return model_path, train_stats

if __name__ == '__main__':
    # Define paths
    config_path = './config/nba_trainig.yaml'
    dataset_path = './data/get_player_game_log_2544_2023-24.csv'
    output_directory = './results'

    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Train model
    model_path, train_stats = train_model(config_path, dataset_path, output_directory)

    # Output model path
    print(f'Model saved to: {model_path}')
    print('Training complete!')
