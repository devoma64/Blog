from django.db import models

# Create your models here.
class Blog(models.Model):
    """A blog the user is writing about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        """Return a simple string representing the blog model"""
        return self.text
    
class Posts(models.Model):
    title = models.ForeignKey(Blog, on_delete=models.CASCADE)
    post = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'posts'
        
    def __str__(self) -> str:
        if len(self.post) > 50:
            return f"{self.post[:50]}..."
        else:
            return f"{self.post}"