﻿using System;
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
	/// Summary description for CodedUITest1
	/// </summary>
	[CodedUITest]
	public class Homepage: TestTemplate
	{
		public Homepage()
		{
		}

		[TestMethod]
					
			public void test1()
			{
				LaunchBrowser_Keep("https://agaveqa.inside.cactussoft.biz",true);
			
			}
		




	}
}
