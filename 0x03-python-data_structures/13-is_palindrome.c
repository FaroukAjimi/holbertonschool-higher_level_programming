#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *is_palindrome - lis
 *@head: jkjkj
 *Return : 0
 */
int is_palindrome(listint_t **head)
{
	int y = 0;
	int i = 0;
	listint_t *tail = *head;

	if (*head == NULL)
		return(1);
	while (tail->next != NULL)
	{
		tail = tail->next;
		i++;
	}
	i = i+1;
	tail = *head;
	while (i > 0)
	{
		while (y != i - 1)
		{
			y++;
			tail = tail->next;
		}
		y = 0;
		if ((*head)->n != tail->n)
		{
			return(0);
		}
		*head = (*head)->next;
		tail = (*head);
		i = i-2;
	}
	return(1);
}
