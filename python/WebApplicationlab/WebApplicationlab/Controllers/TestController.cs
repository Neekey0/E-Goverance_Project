using Microsoft.AspNetCore.Mvc;

namespace WebApplicationlab.Controllers
{
    public class TestController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
