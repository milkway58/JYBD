package pageModle;



import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.Test;

import common.FindElement;



public class BusinessCenter {
	
	public void business(WebDriver driver) {
		
		// TODO Auto-generated method stub
		  FindElement find = new FindElement();     
		   		
//			页面登录成功
//			find.waitWebElement(driver, By.linkText("商品"), 2);
			find.implicitlyWait(driver);//时间等待
			find.byLink(driver, "商品").click();
			find.bySelector(driver,"#mainContent > div > a:nth-child(1)").click();

			find.implicitlyWait(driver);//时间等待
//			润滑油
			find.byLink(driver, "维修保养").click();
			find.byLink(driver, "润滑油").click();			
			find.byLink(driver, "汽机油").click();
		
//			Assert.assertEquals("下一步，填写商品信息", "下一步，填写商品信息","信息查询不到");
//			find.implicitlyWait(driver);
			try {
				Thread.sleep(500);
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}

			find.byXpath(driver, "//*[@id='mainContent']/div/div[3]/form/div/label/input").click();
		
			//		下一步，填写商品信息
//			编辑商品信息

			find.implicitlyWait(driver);//时间等待
			find.byName(driver, "g_name").clear();
			
//			机油
			find.byName(driver, "g_name").sendKeys("测试拼单通润滑油1（结算退款3)");

			
			
			find.byName(driver, "g_costprice").clear();
			find.byName(driver, "g_costprice").sendKeys("0.1");

			find.byName(driver, "g_storage").clear();
			find.byName(driver, "g_storage").sendKeys("500");

			//时间等待

			
//			上传图片---机油
			find.byName(driver, "goods_image").sendKeys("D:/Admin/Pictures/1.jpg");

			try { 
				Thread.sleep(5000);
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		
//			机油
			
			find.byName(driver, "b_name").click();
			find.byLink(driver, "J").click();
			find.bySelector(driver, "div.brand-list.ps-container.ps-active-y > ul > li:nth-child(4)").click();
			
			
//			div.ncsc-brand-select-container > div.brand-list.ps-container.ps-active-y > ul > li:nth-child(9)
//			find.bySelector(driver, "div.brand-list.ps-container.ps-active-y > ul > li:nth-child(4)").click();

			find.bySelector(driver, "[value='下一步，上传商品图片']").click();
			
		
			find.bySelector(driver, "[value='下一步，确认商品发布']").click();
			
			
//			验证商品是否在仓库中待审核
			find.byLink(driver, "仓库中的商品").click();
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			find.byLink(driver, "等待审核的商品").click();
			
		  
	  }

	
	}

