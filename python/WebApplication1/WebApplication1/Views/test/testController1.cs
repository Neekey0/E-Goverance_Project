using Microsoft.AspNetCore.Mvc;

namespace WebApplication1.Views.test
{
    public class testController1 : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
