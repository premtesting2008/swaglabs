package page;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class SauceDemo 
{
	
	public static WebElement Username(WebDriver d)
	{
		WebElement e1 = d.findElement(By.id("user-name"));
		return e1;
	}
	public static WebElement Password(WebDriver d)
	{
		WebElement e2 = d.findElement(By.id("password"));
		return e2;
	}
	
	public static WebElement Login(WebDriver d)
	{
		WebElement e3 = d.findElement(By.name("login-button"));
		return e3;
	}
	public static WebElement AddToCart(WebDriver d)
	{
		WebElement e4 = d.findElement(By.name("add-to-cart-sauce-labs-backpack"));
		return e4;
	}
	public static WebElement CartOpen(WebDriver d)
	{
		WebElement e5 = d.findElement(By.className("shopping_cart_link"));
		return e5;
	}
	public static WebElement CheckOut(WebDriver d)
	{
		WebElement e6 = d.findElement(By.name("checkout"));
		return e6;
	}
	public static WebElement FirstName(WebDriver d)
	{
		WebElement e7 = d.findElement(By.id("first-name"));
		return e7;
	}
	public static WebElement LastName(WebDriver d)
	{
		WebElement e8 = d.findElement(By.id("last-name"));
		return e8;
	}
	public static WebElement ZipCode(WebDriver d)
	{
		WebElement e9 = d.findElement(By.id("postal-code"));
		return e9;
	}
	public static WebElement Continue(WebDriver d)
	{
		WebElement e10 = d.findElement(By.id("continue"));
		return e10;
	}
	public static WebElement Finish(WebDriver d)
	{
		WebElement e11 = d.findElement(By.id("finish"));
		return e11;
	}
	public static WebElement BackHome(WebDriver d)
	{
		WebElement e12 = d.findElement(By.id("back-to-products"));
		return e12;
	}

}
