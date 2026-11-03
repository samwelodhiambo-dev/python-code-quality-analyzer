from pathlib import Path
from analyzer import CodeAnalyzer


def main():
    print("PYTHON CODE QUALITY ANALYZER")
    print("============================")

    file_path = input("Enter Python file path: ")
    path = Path(file_path)

    if not path.is_file():
        print("Error: File not found.")
        return

    source_code = path.read_text(encoding="utf-8")

    analyzer = CodeAnalyzer()
    issues = analyzer.analyze(source_code)

    print("\nCODE QUALITY REPORT")
    print("-------------------")

    if not issues:
        print("No issues found. Great work!")
    else:
        for issue in issues:
            print(
                f"{issue['type']} | "
                f"Line {issue['line']} | "
                f"{issue['message']}"
            )

    print(f"\nTotal issues found: {len(issues)}")


if __name__ == "__main__":
    main()
