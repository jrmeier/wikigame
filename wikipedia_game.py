import wikipedia
import re
import sys

wikipedia.set_rate_limiting(True)


def remove_bad_links(links):
    reg = "((((((\s)|(^)|,|)category:[^,]{2,})(,|))))"
    reg += "|((((((\s)|(^)|,|)template:[^,]{2,})(,|))))" 
    reg += "|((((((\s)|(^)|,|)module:[^,]{2,})(,|))))"
    reg += "|((((((\s)|(^)|,|)wikipedia:[^,]{2,})(,|))))"
    reg += "|((((((\s)|(^)|,|)portal:[^,]{2,})(,|))))"
    reg += "|,$"
    as_string = ",".join(links)
    cleaned = as_string.lower()
    cleaned = re.sub(reg, '', cleaned)

    return cleaned.split(',')


def get_links(name):
    try:
        page = wikipedia.page(name.title())
        return remove_bad_links(page.links)
    except Exception:
        return []


def process_node(node, queue, end, path):
    links = get_links(node)

    for link in links:
        new_path = list(path)
        new_path.append(link)
        queue.append(new_path)

        if link == end:
            return {'is_found': True, 'path': new_path}

    return {'links': links, 'is_found': False, 'queue': queue}


def format_return(path, depth, is_found=False):
    return {
            'path': path,
            'pretty_path': ' -> '.join(path).title(),
            'depth': depth,
            'is_found': str(is_found)
            }


def fn_queue(queue, visited, end, show_updates, depth=1):
    path = queue.pop(0)
    node = path[-1]

    if show_updates:
        if len(path) > depth:
            formatted = format_return(path, depth)
            print(formatted)

    depth = len(path)
    if node not in visited:
        result = process_node(node, queue, end, path)
        if result.get('is_found'):
            return format_return(result.get('path'), depth, True)

        visited.append(node)
        queue = result.get('queue')
    return fn_queue(queue, visited, end, show_updates, depth)


def run(start, end, show_updates=False):
    start = start.lower()
    end = end.lower()
    start = start.strip()
    end = end.strip()

    visited = []
    queue = [[start]]

    while queue:
        return fn_queue(queue, visited, end, show_updates)

    return {'is_found': False}


if __name__ == "__main__":
    start = sys.argv[1]
    end = sys.argv[2]
    ret = run(start, end)
    if ret.get('is_found', None):
        print(ret.get('pretty_path'))
    else:
        print("Sorry, I couldnt find that path")
