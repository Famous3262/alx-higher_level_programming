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
	listint_t *temp, *rev, *mid;
	size_t size = 0, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (j = 0; j < (size / 2) - 1; j++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rev = reverse_listint(&temp);
	mid = rev;

	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
