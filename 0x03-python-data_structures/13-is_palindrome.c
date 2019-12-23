#include "lists.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stddef.h>
/**
 *is_palindrome - prints a list length
 *@head: the first position
 *Return: On success 1.
*/

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int i = 0, cnt = 0;
	int arr[2500];

	if (!head)
		return (0);

	if (*head == NULL)
		return (1);

	while (tmp)
	{
		arr[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	while ((i / 2) >= 0)
	{
		if (arr[cnt] != arr[i - 1])
		{
			return (0);
		}
		else
		{
			i--;
			cnt++;
		}
	}
	return (1);
}
