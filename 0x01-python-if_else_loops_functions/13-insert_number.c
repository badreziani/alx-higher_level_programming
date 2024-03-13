#include "lists.h"

/**
 * insert_node - inserts a node in linked list
 * @head: points the first node in the list
 * @number: the number to insert in the list
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	tmp = *head;
	if (!tmp)
	{
		*head = new;
		return (new);
	}
	if (tmp->n > new->n)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}
	while (tmp)
	{
		if(!tmp->next)
		{
			tmp->next = new;
			return (tmp);
		}
		else if (tmp->n > new->n)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	return (NULL);
}
