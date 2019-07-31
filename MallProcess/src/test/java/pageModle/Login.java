package pageModle;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import common.FindElement;
import common.GetScreenshotAs;
/*@author: 
 *    
 *    
 * 
 * 
 * */


public class Login{
	
	
   //商家中心
	public  void Business(WebDriver driver,String url,String name,String pwd,String captcha) {
		 driver.manage().window().maximize();
		 driver.manage().timeouts().implicitlyWait(15,TimeUnit.SECONDS);
		 
		 
		 driver.get(url);
		 FindElement find = new FindElement();
		 find.byLink(driver, "商家管理登录").click();
		 find.byName(driver, "seller_name").sendKeys(name);//
		 find.byName(driver, "password").sendKeys(pwd);
		find.byName(driver,"captcha").sendKeys(captcha);
		GetScreenshotAs screen=new GetScreenshotAs();
		screen.Screen(driver);
		find.byclassName(driver,"login-submit").click();
		
		
	}
	
	
	//	系统管理中心
	
	public  void admin(WebDriver driver,String url,String name,String pwd) {
		 driver.manage().window().maximize();
		 driver.manage().timeouts().implicitlyWait(15,TimeUnit.SECONDS);
		 //	系统管理中心
		 
		 driver.get(url);
		 FindElement find = new FindElement();
		 //find.byLink(driver, "商家管理登录").click();
		 find.byId(driver, "user_name").sendKeys(name);
		 find.byId(driver, "password").sendKeys(pwd);
		 find.byId(driver,"captcha").sendKeys("ichs");
		GetScreenshotAs screen=new GetScreenshotAs();
		screen.Screen(driver);
		find.byclassName(driver,"btn-submit").click();
		
		
	}
	
	
	//前台
	
	public  void frontdesk(WebDriver driver,String url,String username,String pwd) {
		 driver.manage().window().maximize();
		 driver.manage().timeouts().implicitlyWait(15,TimeUnit.SECONDS);
		 //	前台
		 
		
		 	
		    driver.navigate().refresh();
		    FindElement find = new FindElement();
		    find.byXpath(driver, "//a[text()='登录']").clear();
			driver.manage().timeouts().implicitlyWait(50, TimeUnit.SECONDS);
			find.byclassName(driver,"text").sendKeys(username);
			find.byName(driver,"password").sendKeys(pwd);
			find.byName(driver,"captcha").sendKeys("ichs");
			find.byclassName(driver,"submit").click();
			//driver.findElement(By.className("text")).sendKeys(username);
			//driver.findElement(By.name("password")).sendKeys(pwd);
			//driver.findElement(By.name("captcha")).sendKeys("ichs");
			//driver.findElement(By.className("submit")).click();
			// 返回前一页面
			// driver.navigate().back();
		
		
	}
}
