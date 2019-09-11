#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert item into sorted linked list
 * @head: pointer to head pointer
 * @number: number to insert
 * Return: pointer to inserted item, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	if (!head)
		return (NULL);

	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;

	if (!*head)
		return (*head = new);
	/* If new item belongs at beginning of list */
	if (number <= (*head)->n)
	{
		new->next = *head;
		return (new);
	}
	/* Search for position */
	listint_t *prev = *head, *curr = prev->next;

	while (curr)
	{
		if (curr->n >= number)
			break;
		prev = curr;
	   curr = curr->next;
	}
	prev->next = new;
	new->next = curr; /* `curr` is null if new item belongs at end */
	return (new);
}
