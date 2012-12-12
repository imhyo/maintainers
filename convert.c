#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE *fp;
	char str[256];
	int beginning = 1;
	int maintainer = 0, f = 0, driver = 0;
	int len = 0;

	fp = fopen("./Maintainers.txt", "rt");

	while (fgets(str, 256, fp))
	{
		if (str[0] == '\n' || str[0] == ' ' || str[0] == 0)
		{
			if (driver)
				printf("\tD");
			beginning = 1;
			maintainer = f = driver = 0;
			printf("\n");
			continue;
		}

		len = strlen(str);
		if (str[len - 1] == '\n') str[len - 1] = 0;

		if (beginning)
		{
			beginning = 0;
			maintainer = f = 0;
			printf(str);
			continue;
		}

		if (str[0] == 'M')
		{
			if (maintainer)
				printf(", ");
			else
				printf("\t");
			printf(str + 3);
			maintainer = 1;
			f = 0;
			continue;
		}
		
		maintainer = 0;
	
		if (str[0] == 'F')
		{
			if (f)
				printf(", ");
			else
				printf("\t");
			printf(str + 3);
			f = 1;
			if (strncmp(str + 3, "drivers", 7) == 0)
				driver = 1;
		}
		else
			f = 0;
	}

	fclose(fp);

	return 0;
}

