import wandb

print(f'Currently using version {wandb.__version__} of wandb.')

assert wandb.__version__ == '0.15.1', f'Expected 0.15.2, but got {wandb.__version__}'
