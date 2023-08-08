#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle using
 *
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't.
 */
int check_cycle(listint_t *list)
{
	listint_t *lag = list;
	listint_t *quick = list;

	if (!list)
		return (0);

	while (lag && quick && quick->next)
	{
		lag = lag->next;
		quick = quick->next->next;
		if (lag == quick)
			return (1);
	}

return (0);
}
