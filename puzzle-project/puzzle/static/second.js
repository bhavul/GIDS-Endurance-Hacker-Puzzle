/**
 * Created by bhavul.g on 18/04/17.
 */

function submitDetailsForm(){
    if($("#username").val() == 'johndoe')
    {
        console.log("correct username chosen")
        $("#form").submit()
    }
    else
    {
        console.log("That username was wrong. Please try again.")
        window.location.reload();
    }
}
