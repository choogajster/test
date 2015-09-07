using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.Windows.Input;
using System.Windows.Forms;
using System.Drawing;
using Microsoft.VisualStudio.TestTools.UITesting;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Microsoft.VisualStudio.TestTools.UITest.Extension;
using Keyboard = Microsoft.VisualStudio.TestTools.UITesting.Keyboard;


namespace WispTestProject
{
	/// <summary>
	/// Summary description for TestTemplate
	/// </summary>
	[CodedUITest]

	public class TestTemplate
	{

		public string testName = "";
		public string moduleName = "";
		protected static BrowserWindow browser;
		//public static RemoteWebDriver driver;

		public void NullifyWindow()
		{
			browser = null;

		}

		public void BrowserValidationAndRun(string email, string password)
		{
			if (browser == null)
			{
				LaunchBrowser_Keep(Parameters.QaServer, Parameters.CloseBrowser);
				//Login(email, password);


			}
			else
			{
				NullifyWindow();
			}

		}

		public void LaunchBrowser_Keep(string url, bool cleanup)
		{
			BrowserWindow.CurrentBrowser = Parameters.browser;
			browser = BrowserWindow.Launch(new Uri(url));
			browser.CloseOnPlaybackCleanup = cleanup;
			if (Parameters.browser == "ie")
			{
				browser.Maximized = true;
			}


		}
	}
}
