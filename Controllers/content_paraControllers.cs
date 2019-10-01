using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using Microsoft.AspNetCore.Hosting.Internal;
using Microsoft.AspNetCore.Mvc;
namespace Intro2MVC.Controllers
{
    public class EmployeeController : Controller
    {
        public HostingApplication _wha
        }
        //Get: Employee/Index
        public IActionResult Index()
        {
            return View();
        }
        
        //Get: Employee/Create
        public IActionResult Create()
        {
            return View();
        }

        public IActionResult Save(string firstName, string lastName, int age,
                                    string nationalInsuranceNo, string gender,
                                    string address, double monthlySalary)
        {
        
        //oof what the fuck is the even just supposed to mean anyway
       