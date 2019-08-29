# import wikipedia
import re
import sys

import wikipediaapi
wiki = wikipediaapi.Wikipedia('en')

from multiprocessing import Pool
# wikipedia.set_rate_limiting(True)
from collections import deque


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


# def get_links(name):
#     try:
#         page = wikipedia.page(name.title())
#         return remove_bad_links(page.links)
#     except Exception:
#         return []

def get_links(id):
    # print("getting links for: ",name)

    try:
        page = wiki.page(name)
        return remove_bad_links(wiki.page(name).links)
    except Exception as e:
        return []

def get_id(name):
  try:
    return wiki.page(name).pageid
  except Exception:
    return []

def process_node(node, queue, end, path):
    links = get_links(node)
    # print("processing: ",)
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
            # 'pretty_path': ' -> '.join(path).title(),
            'depth': depth,
            'is_found': str(is_found)
            }


def fn_queue(queue, visited, end, show_updates, depth=1):
    if queue:
        # print("queue len: ",len(queue))

        # path = queue.popleft()
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



        return fn_queue(queue, visited, end, show_updates, depth)
    return { 'is_found': False }


def run(start, end, show_updates=True):
    start = get_id(start)
    end = get_id(end)

    visited = []
    # queue = deque([[start]])
    queue = [[start]]

    return fn_queue(queue, visited, end, show_updates)



if __name__ == "__main__":
    # ret = get_links('Web Bot')
    # print(ret)
    # p = Pool()
    start = sys.argv[1]
    end = sys.argv[2]
    ret = run(start, end)
    # print(ret)
    if ret.get('is_found', None):
        print(ret.get('path'))
    else:
        print("Sorry, I couldnt find that path")


