import os
import secrets
import string

def generate_secret_key():
    """Generates a secure random 50-character string."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*(-_=+)"
    return "".join(secrets.choice(chars) for _ in range(50))

def setup_project():
    print("🚀 Initializing your new Django project...")
    
    # 1. Collect inputs
    new_site_name = input("Enter Site Name (e.g., My New App): ").strip()
    
    # 2. Configuration placeholders (must match your boilerplate) [cite: 129]
    old_site_name = "New Project" 
    env_file = ".env"
    
    # 3. Process all project files for Site Name [cite: 1, 6, 7]
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        # Ignore Git, Virtual Environments, and Caches 
        if any(skip in root for skip in ['.git', 'venv', '__pycache__']):
            continue
            
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            # Skip binary files like db.sqlite3
            if file_name.endswith(('.sqlite3', '.pyc', '.png', '.jpg')):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update SITE_NAME in files like settings/base.py and layouts/base.html [cite: 68, 129]
                if old_site_name in content:
                    new_content = content.replace(old_site_name, new_site_name)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
            except Exception as e:
                print(f"⚠️  Could not process {file_name}: {e}")

    # 4. Handle .env file and Secret Key 
    if os.path.exists(env_file):
        new_key = generate_secret_key()
        with open(env_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        with open(env_file, 'w', encoding='utf-8') as f:
            for line in lines:
                if line.startswith("SECRET_KEY"):
                    f.write(f'SECRET_KEY="{new_key}"\n')
                elif line.startswith("DEBUG"):
                    f.write("DEBUG=True\n") # Default to Dev mode 
                else:
                    f.write(line)
        print(f"✅ Generated new SECRET_KEY in {env_file}")

    print(f"\n✨ Project '{new_site_name}' is ready to go!")

if __name__ == "__main__":
    setup_project()