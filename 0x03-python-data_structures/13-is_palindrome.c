#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: point to the first node of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *middle, *prev, *one_step, *two_steps;

	if (!(*head))
		return (1);
	one_step = *head;
	two_steps = *head;
	while (1)
	{
		if (!two_steps || !two_steps->next)
			break;
		prev = one_step;
		one_step = one_step->next;
		two_steps = two_steps->next->next;
	}
	if (!two_steps)
		middle = one_step;
	else
		middle = one_step->next;
	prev->next = NULL;
	middle = reverse_listint(&middle);
	while (middle)
	{
		if ((*head)->n != middle->n)
			return (0);
		*head = (*head)->next;
		middle = middle->next;
	}
	return (1);
}
