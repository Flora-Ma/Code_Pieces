from enum import Enum
import heapq
import time

class CacheStrategy(Enum):
    LRU = 1
    FIFO = 2

#print(CacheStrategy.FIFO)
#print(CacheStrategy(1))
#print(CacheStrategy.FIFO.value)

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity=10):
        self.store = dict()
        self.capacity = capacity
        self.list_head = Node(None) # doubly linked list
        self.key_node_map = dict()

    def add(self, key, value):
        print(f'Add key={key}, value={value}')
        if key in self.store:
            print(f'Key {key} is already in cache. Use update if you\'d ' 
                            + 'like to update its value.')
            return
        self.store[key] = value
        node = Node(key)
        self.key_node_map[key] = node
        self.__add_node_to_head(node)
        self.__print_list()
        if len(self.store) > self.capacity:
            node = self.list_head.prev
            self.__remove_node(node)
            self.store.pop(node.value)
        self.__print_list()

    def get(self, key):
        print(f'Get key={key}')
        if key not in self.store:
            print(f'Missed Key={key}')
            return 
        node = self.key_node_map[key]
        self.__remove_node(node)
        self.__add_node_to_head(node)
        self.__print_list()
        return self.store[key]

    def update(self, key, value):
        print(f'Update key={key}, value={value}')
        if key not in self.store:
            raise Exception(f'Missed Key={key}')
        self.store[key] = value
        node = self.key_node_map[key]
        self.__remove_node(node)
        self.__add_node_to_head(node)
        self.__print_list()    
    
    def delete(self, key):
        print(f'Delete key={key}')
        if key not in self.store:
            raise Exception(f'Missed Key={key}')
        self.store.pop(key)
        node = self.key_node_map[key]
        self.__remove_node(node)
        self.__print_list()

    def __print_list(self):
        print('Forward:')
        node = self.list_head.next
        while node != self.list_head:
            print(node.value, end=',')
            node = node.next
        print('\nBackward:')
        node = self.list_head.prev
        while node != self.list_head:
            print(node.value, end=',')
            node = node.prev
        print()

    def __remove_node(self, node):
        pre_node = node.prev
        next_node = node.next
        pre_node.next = next_node
        next_node.prev = pre_node

    def __add_node_to_head(self, node):
        node.prev = self.list_head
        node.next = self.list_head.next
        self.list_head.next = node
        if node.next == None:
            node.next = self.list_head
        node.next.prev = node

# Test LRUCache
lru_cache = LRUCache(3)
lru_cache.add(1, 1)
lru_cache.add(2, 2)
lru_cache.add(3, 3)
lru_cache.update(2, 22)
print(lru_cache.get(1))
lru_cache.add(4, 4)
print(lru_cache.get(3)) # print missed key
lru_cache.delete(4)
lru_cache.add(5, 5)
lru_cache.add(6, 6)
lru_cache.update(2, 222) # error




