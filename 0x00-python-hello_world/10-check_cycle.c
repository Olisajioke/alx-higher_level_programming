#include "lists.h"


/**
 * check_cycle - Checks if a singly linked list has a
 * cycle in it using Floyd's cycle detection algorithm.
 *
 * @list:A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 if there is no cycle.
 */


int check_cycle(struct listint_t *list)
{
	if (list == NULL)
	{
	return (0);
	}

	struct listint_t *quick_case = list;
	struct listint_t *slow_case = list->next;

	while (slow_case != NULL && slow_case->next != NULL)
	{
	if (quick_case == slow_case)
	{
	return (1);
}	quick_case = quick_case->next;
	slow_case = slow_case->next->next;
}
return (0);
}
