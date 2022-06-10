using Microsoft.AspNetCore.Mvc;

namespace WebApplication1.Controllers
{
    public class employeeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
