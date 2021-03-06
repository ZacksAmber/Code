#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: Databricks.py                                                         #
# File: /Users/zacks/Desktop/Code/Python/Databricks/Databricks.py              #
# Project: /Users/zacks/Desktop/Code/Python/Databricks                         #
# Created Date: 2020-09-22                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-10-29 8:50:45 pm                                         #
# Modified By: Zacks Shen <zacks.shen@pluralpoint.com>                         #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        currentNode = self # current node will be initialized to be self. At the begining, the current node is the node that we called the insertion method on and that's self.
        while True:
            if value < currentNode.value:
                if currentNode.left is None: # it means we are at the end of the branch
                    currentNode.left = BST(value) # insert the value
                    break
                else: # meaning we still have a left subtree to explore
                    currentNode = currentNode.left # then we go back to the while definition
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right # then we go back to the while definition
            
            return self # allow us call the insert function, kind of one after the other during test cases
            # testBest.insert(1).insert(5)

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        # Write your code here.
        currentNode = self
        while currentNode is not None: # if none, return False
            if value < currentNode.value: # it is equal to remove the right subtree, and repeat the loop
                currentNode = currentNode.left 
            elif value > currentNode.value: # in this case, we explore the right subtree
                currentNode = currentNode.right
            else: # if value == currentNode.value, which means we find the value
                return True
        return False 

    def remove(self, value, parentNode = None): # if you remove the root node of the BST, there is no parent node.
        # Write your code here.
        # Do not edit the return statement of this method.
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value: # skip the right subtree
                parentNode = currentNode # cause when we update the current node, the parent node becomes the node that we just exploring.
                currentNode = currentNode.left # loop
            elif value > currentNode.value: # skip the left subtree
                parentNode = currentNode
                currentNode = currentNode.right # loop
            else: # the removing process, but we cannot simply remove it, we need consider more 
                if currentNode.left is not None and currentNode.right is not None: # both the children nodes aren't null values
                    currentNode.value = currentNode.right.getMinValue() # replace the current node value to the minimum value of the subtree of the current node
                    # currentNode.value = smallest value of right subtree
                    currentNode.right.remove(currentNode.value, currentNode) # invoke the remove function, notice the parameters
                # we're gonna come back to the root node case
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        # this is a single-node tree; do nothing.
                        pass
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        
        return currentNode.value