package common;
/**
 * 元素查找定位，从这类调用
 * @author：wangtong
 * @date：2018年7月23日
 */
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.WebDriverWait;

public class FindElement {//
	public  void set_Url(WebDriver driver,String url){
		driver.get(url);
	}
	public void implicitlyWait(WebDriver driver){
		driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS);
	}
	
	public WebElement byId(WebDriver driver,String id){
		
		return driver.findElement(By.id(id));
		
	}
	
	public WebElement byName(WebDriver driver,String name){
		
		 return driver.findElement(By.name(name));
	}
	
	public WebElement byLink(WebDriver driver,String link){
		
		return driver.findElement(By.linkText(link));
	}
    public WebElement bypartialLink(WebDriver driver,String partial){
		
		return driver.findElement(By.partialLinkText(partial));
	}
	
	
	public WebElement byXpath(WebDriver driver,String xpath){
		
		return driver.findElement(By.xpath(xpath));
		}
	public WebElement bySelector(WebDriver driver,String selector){
		
		return driver.findElement(By.cssSelector(selector));
	}
    public WebElement byclassName(WebDriver driver,String className){
		
		return driver.findElement(By.className(className));
	}
	//窗口切换
	public void switchWindow(WebDriver driver){
		driver.close();
		for(String handle:driver.getWindowHandles()){
			driver.switchTo().window(handle);
			break;
		}	
	}
//	时间等待加载
	public static WebElement waitWebElement(WebDriver driver, final By by, int second) {
	    WebElement waitElement = null;
	    WebDriverWait wait = new WebDriverWait(driver, second);
	    try {
	        // 创建一个新的ExpectedCondition接口，实现apply方法
	        waitElement = wait.until(new ExpectedCondition<WebElement>(){
	            public WebElement apply(WebDriver d) {
	                return d.findElement(by);
	            }
	        });
	    } catch (Exception e) {
	        System.out.println(by.toString() + " is not exist until " + second);
	    }
	    return waitElement;
	}
	
	
	public static WebElement PageLoad (WebDriver driver,int second){
		return	(WebElement) driver.manage().timeouts().pageLoadTimeout(second,TimeUnit.SECONDS);}
	
}
