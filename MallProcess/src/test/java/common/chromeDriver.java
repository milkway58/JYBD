package common;

import org.openqa.selenium.chrome.ChromeDriver;

public class chromeDriver {
	private chromeDriver(){
    }
    private static volatile ChromeDriver driver = null;
    public static ChromeDriver getDriver() {
        if (driver == null) {
            synchronized(chromeDriver.class) {
                    driver = new ChromeDriver();
                
            }
        }
        return driver;
    }
}
//synchronized 关键字是用来控制线程同步的，就是在多线程的环境下，控制synchronized代码段不被多个线程同时执行
// volatile     https://www.cnblogs.com/zhengbin/p/5654805.html
//    synchronized  https://www.cnblogs.com/QQParadise/articles/5059824.html