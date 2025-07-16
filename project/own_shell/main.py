import sys
import os
import subprocess

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        c = command.strip().split()

        if not c:
            continue
        
        if c[0] == "exit":
            if len(c) > 1 and c[1].isdigit():
                sys.exit(int(c[1]))
            else:
                sys.exit()

        if c[0] == "echo":
            sys.stdout.write(" ".join(c[1:]) + "\n")
            continue

        if c[0] == "type" and len(c) > 1:
            for e in c[1:]:
                if e == "echo":
                    print("echo is a shell builtin")
                elif e == "exit":
                    print("exit is a shell builtin")
                elif e == "type":
                    print("type is a shell builtin")
                else:
                    found = False
                    for path in os.getenv("PATH").split(os.pathsep):
                        if os.path.isdir(path):
                            if e in os.listdir(path):
                                print(f"{e} is {path}/{e}")
                                found = True
                                break
                    if not found:
                        print(f"{e}: not found")
            continue
        
        try:
            result = subprocess.run(c, capture_output=True, text=True)
            if result.stdout:
                print(result.stdout, end="")
            if result.stderr:
                print(result.stderr, end="")
        except FileNotFoundError:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
