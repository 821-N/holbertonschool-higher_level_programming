#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * list_length - get length of linked list
 * @head: head ptr
 * Return: length
 */
size_t list_length(listint_t *head)
{
	size_t len;

	for (len = 0; head; len++)
		head = head->next;
	return (len);
}

/**
 * reverse_until - reverse part of a linked list
 * @start: start of section to reverse
 * @end: node to stop at (NULL for end of list)
 * Return: pointer to last node
 * To fix a list after reversing, just call reverse_until(last, NULL)
 */
listint_t *reverse_until(listint_t *start, listint_t *end)
{
	listint_t *prev = NULL, *nx;

	while (start != end)
	{
		nx = start->next;
		start->next = prev;
		prev = start;
		start = nx;
	}
	return (prev);
}

/**
 * is_palindrome - check if linked list is palindrome
 * @head: address of head ptr
 * Return: 0 (not palidrome) or 1 (palindrome)
 */
int is_palindrome(listint_t **head)
{
	size_t len, i;
	listint_t *mid, *end, *temp1, *temp2;
	int ret = 1;

	if (!head)
		return (0);

	len = list_length(*head); /* idea: find middle using tortoise/hare thing */
	mid = *head;
	for (i = 0; i < (len + 1) / 2; i++)
		mid = mid->next;
	end = reverse_until(mid, NULL);
	temp1 = *head;
	temp2 = end;
	for (i = 0; i < len / 2; i++)
	{
		if (temp1->n != temp2->n)
		{
			ret = 0;
			break;
		}
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	reverse_until(end, NULL);
	return (ret);
}
