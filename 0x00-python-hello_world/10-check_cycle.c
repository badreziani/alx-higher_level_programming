#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *x, *xx;

	x = list;
	xx = list;
	while (x && xx && xx->next)
	{
		x = x->next;
		xx = xx->next->next;
		if (x == xx)
			return (1);
	}
	return (0);
}
