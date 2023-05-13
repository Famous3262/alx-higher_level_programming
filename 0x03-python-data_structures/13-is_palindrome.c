#include "lists.h"

/**
 * reverse_listint - A function that reverses a linked list
 * @head: Pointer to the first node
 *
 * Return: Points to the first node in a new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*head = prev;
}

/**
 * is_palindrome - This function checks if a linked list is a palindrome
 * @head: A pointer to the head of a linked list
 *
 * Return: 1 if it is a palindrome, 0 if it is not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *back = *head, *fwd = *head, *temp = *head, *mid = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fwd = fwd->next->next;
		if (!fwd)
		{
			mid = back->next;
			break;
		}
		if (!fwd->next)
		{
			mid = back->next->next;
			break;
		}
		back = back->next;
	}

	reverse_listint(&mid);

	while (mid && temp)
	{
		if (temp->n == mid->n)
		{
			mid = mid->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!mid)
		return (1);

	return (0);
}
