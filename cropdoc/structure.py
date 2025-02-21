import os

def create_directories(base_path="cropdoc"):
    directories = [
        "data/raw",
        "data/processed",
        "data/augmented",
        "data/splits",
        "models/cashew/training",
        "models/cashew/saved_models",
        "models/cashew/evaluation",
        "models/cinnamon",
        "models/maize",
        "models/tomato",
        "research/notebooks",
        "cloud/api_gateway",
        "cloud/inference",
        "cloud/storage",
        "cloud/monitoring",
        "web/frontend/public",
        "web/frontend/src",
        "web/frontend/tests",
        "web/backend/routes",
        "web/backend/utils",
        "web/backend/database",
        "llm/prompts",
        "llm/responses",
        "llm/validation",
        "tests/unit_tests",
        "tests/integration_tests",
        "tests/user_testing",
        "docs/user_guide",
        "docs/api_docs",
        "docs/technical",
        "scripts"
    ]
    
    for directory in directories:
        path = os.path.join(base_path, directory)
        os.makedirs(path, exist_ok=True)
        print(f"Created: {path}")
    
    # Create default files
    default_files = [
        "research/utils.py",
        "research/exception.py",
        "research/logger.py",
        "research/env",
        "research/main.py",
        "requirements.txt",
        "structure.py"
    ]
    
    for file in default_files:
        path = os.path.join(base_path, file)
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write("")
            print(f"Created: {path}")
    
    print("Project structure created successfully!")

if __name__ == "__main__":
    create_directories()
