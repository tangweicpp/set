#include<stdio.h>
#include<bcm2835.h>

#define IN1 RPI_BPLUS_GPIO_J8_11
#define IN2 RPI_BPLUS_GPIO_J8_12
#define IN3 RPI_BPLUS_GPIO_J8_16
#define IN4 RPI_BPLUS_GPIO_J8_18

void forward()
{
	bcm2835_gpio_write(IN1, HIGH);
	bcm2835_gpio_write(IN2, LOW);
	bcm2835_gpio_write(IN3, HIGH);
	bcm2835_gpio_write(IN4, LOW);
}

int main()
{
	if( !bcm2835_init() )
	{
		return 1;
	}

	bcm2835_gpio_fsel(IN1, BCM2835_GPIO_FSEL_OUTP);
	bcm2835_gpio_fsel(IN2, BCM2835_GPIO_FSEL_OUTP);
	bcm2835_gpio_fsel(IN3, BCM2835_GPIO_FSEL_OUTP);
	bcm2835_gpio_fsel(IN4, BCM2835_GPIO_FSEL_OUTP);
	printf("000000000000\n");
	forward();
	printf("111111111111\n");
	bcm2835_delay(500);
	printf("2222222222\n");
	int ret = bcm2835_close();
	if(ret == 1)
	{
		printf("successful\n");
	}
	printf("33333333\n");
	return 1;
}
