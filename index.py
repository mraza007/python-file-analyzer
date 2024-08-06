#!/usr/bin/env python

import ast
import sys
import os
from collections import defaultdict
import importlib
import json


class ReferenceTracker(ast.NodeVisitor):
    def __init__(self):
        self.functions = {}
        self.variables = defaultdict(lambda: {"defined": [], "used": []})
        self.function_calls = defaultdict(list)
        self.classes = {}
        self.imports = []

    def visit_FunctionDef(self, node):
        self.functions[node.name] = {
            "line": node.lineno,
            "args": [arg.arg for arg in node.args.args],
            "returns": self.get_return_type(node),
            "calls": [],
            "docstring": ast.get_docstring(node),
        }
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.classes[node.name] = {
            "line": node.lineno,
            "methods": [m.name for m in node.body if isinstance(m, ast.FunctionDef)],
        }
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append(
                {
                    "name": alias.name,
                    "line": node.lineno,
                    "doc_link": self.get_import_doc_link(alias.name),
                }
            )

    def visit_ImportFrom(self, node):
        for alias in node.names:
            full_name = f"{node.module}.{alias.name}"
            self.imports.append(
                {
                    "name": full_name,
                    "line": node.lineno,
                    "doc_link": self.get_import_doc_link(full_name),
                }
            )

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.variables[node.id]["defined"].append(node.lineno)
        elif isinstance(node.ctx, ast.Load):
            self.variables[node.id]["used"].append(node.lineno)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.function_calls[node.func.id].append(node.lineno)
        self.generic_visit(node)

    @staticmethod
    def get_import_doc_link(import_name):
        try:
            module = importlib.import_module(import_name.split(".")[0])
            return f"https://docs.python.org/3/library/{module.__name__}.html"
        except ImportError:
            return "No documentation link available"

    @staticmethod
    def get_return_type(node):
        return_nodes = [n for n in node.body if isinstance(n, ast.Return)]
        if return_nodes and hasattr(return_nodes[0], "annotation"):
            return ast.unparse(return_nodes[0].annotation)
        return "Unknown"


def analyze_python_file(file_path):
    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)
    tracker = ReferenceTracker()
    tracker.visit(tree)

    return {
        "file_path": file_path,
        "num_lines": len(code.splitlines()),
        "functions": tracker.functions,
        "classes": tracker.classes,
        "imports": tracker.imports,
        "variables": tracker.variables,
        "function_calls": tracker.function_calls,
    }


def print_file_analysis_terminal(analysis):
    print(f"Analysis of {analysis['file_path']}:")
    print(f"Number of lines: {analysis['num_lines']}")

    print("\nFunctions:")
    for name, info in analysis["functions"].items():
        print(
            f"- {name}({', '.join(info['args'])}) -> {info['returns']} (line {info['line']})"
        )
        if info["docstring"]:
            print(f"  Docstring: {info['docstring'].split()[0]}...")
        else:
            print("  No docstring found")
        if info["calls"]:
            print(f"  Called on lines: {', '.join(map(str, info['calls']))}")

    print("\nClasses:")
    for name, info in analysis["classes"].items():
        print(f"- {name} (line {info['line']})")
        for method in info["methods"]:
            print(f"  - {method}")

    print("\nImports:")
    for imp in analysis["imports"]:
        print(f"- {imp['name']} (line {imp['line']})")
        print(f"  Documentation: {imp['doc_link']}")

    print("\nVariables:")
    for var, info in analysis["variables"].items():
        defined = ", ".join(map(str, info["defined"]))
        used = ", ".join(map(str, info["used"]))
        print(f"- {var}:")
        print(f"  Defined on lines: {defined}")
        print(f"  Used on lines: {used}")

    print("\nFunction Calls:")
    for func, calls in analysis["function_calls"].items():
        print(f"- {func}: called on lines {', '.join(map(str, calls))}")


def generate_json_report(analysis):
    return json.dumps(analysis, indent=2)


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python analyzer.py <path_to_python_file_or_project> [--json]")
        sys.exit(1)

    path = sys.argv[1]
    output_json = len(sys.argv) == 3 and sys.argv[2] == "--json"

    if os.path.isfile(path):
        if not path.endswith(".py"):
            print(f"Error: {path} is not a Python file")
            sys.exit(1)
        analysis = analyze_python_file(path)
        if output_json:
            print(generate_json_report(analysis))
        else:
            print_file_analysis_terminal(analysis)
    else:
        print(f"Error: {path} is not a valid file")
        sys.exit(1)
