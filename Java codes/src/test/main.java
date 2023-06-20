package test;

import org.openqa.selenium.chrome.ChromeDriver;

import page.SauceDemo;

public class main
{
	public static void main(String[] args)
	{
		
		google();
	}
	
	public static void google()
	{
		ChromeDriver d = new ChromeDriver();
		d.get("https://www.saucedemo.com/");
		
		SauceDemo.Username(d).sendKeys("standard_user");
		SauceDemo.Password(d).sendKeys("secret_sauce");
		SauceDemo.Login(d).click();
		SauceDemo.AddToCart(d).click();
		SauceDemo.CartOpen(d).click();
		SauceDemo.CheckOut(d).click();
		SauceDemo.FirstName(d).sendKeys("Prem");;
		SauceDemo.LastName(d).sendKeys("Kandela");;
		SauceDemo.ZipCode(d).sendKeys("560076");
		SauceDemo.Continue(d).click();
		SauceDemo.Finish(d).click();
		SauceDemo.BackHome(d).click();	
	}

}
