import java.util.ArrayList;

public class Course
{
    String courseID;
    String courseName;
    ArrayList periods = new ArrayList<Integer>();
    public Course(String courseID, String courseName, ArrayList<Integer>() periods)
    {
        this.courseID = courseID;
        this.periods = periods;
    }
}