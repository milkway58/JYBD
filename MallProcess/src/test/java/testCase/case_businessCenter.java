package testCase;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import common.FileWriter;
import common.GetScreenshotAs;

import common.chromeDriver;
import pageModle.BusinessCenter;
import pageModle.Login;

public class case_businessCenter {
	
	
	
	//商家中心后台
      //登录
	
	
	@Test(dataProvider = "dp")
	public static void case_businessCenter(String name,String pwd) {
		String url = "http://hebing.jybd.cn/chainsell";
		
		WebDriver driver =new ChromeDriver();
		String captcha ="ichs";
		Login login = new Login();
		login.Business(driver, url, name, pwd, captcha);
		String a = "商家中心";
		String text = driver.findElement(By.xpath("/html/body/header/div/div[2]/h1")).getText();
		FileWriter file = new FileWriter();
		if (a.equals(text)) {

			file.createFile("测试点：发布商品     测试结果：通过");

		} else {
			file.createFile("测试点：发布商品     测试结果：失败");

		}
		BusinessCenter businessCenter = new BusinessCenter();
		businessCenter.business(driver);
		GetScreenshotAs screen1 = new GetScreenshotAs();
		screen1.Screen(driver);
		try {
			Thread.sleep(5000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		driver.quit();
	}
	
	
	


	@DataProvider
	public Object[][] dp() {
		return new Object[][] { new Object[] {"jybd6666", "123456" }, new Object[] { "chezhijia", "123456" }, };
	}

}
