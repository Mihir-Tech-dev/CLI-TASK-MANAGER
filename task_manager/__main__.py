from task_manager.manager import TaskManager
import argparse
from typing import Optional

if __name__ == "__main__":
    tm = TaskManager()
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.add_argument("--priority", type=str, choices=["low", "medium", "high"],
    default="medium")

    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type=int)

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--filter", type=str, choices=["todo", "done"], default=None)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        print(f"Adding: {args.title} with priority [{args.priority}]")
        tm.add(args.title, args.priority)

    elif args.command == "done":
        print(f"Marking #{args.id} as done")
        tm.complete(args.id)

    elif args.command == "list":
        print(f"listing all the tasks")
        tm.list_task(args.filter)

    elif args.command == "delete":
        print(f"deleting #{args.id}")
        tm.delete(args.id)