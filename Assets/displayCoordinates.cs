using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class displayCoordinates : MonoBehaviour
{
    public GameObject headset;
    public GameObject leftController;
    public GameObject rightController;
    public TMP_Text coordinateText;
    Vector3 leftControllerPosition;
    Vector3 rightControllerPosition;
    Vector3 headsetPosition;
    // Start is called before the first frame update
    void Start()
    {
        headset = GameObject.Find("CenterEyeAnchor");
    }

    // Update is called once per frame
    void Update()
    {
        headsetPosition = headset.transform.position;
        leftControllerPosition = leftController.transform.position;
        rightControllerPosition = rightController.transform.position;

        // var leftDistance = Vector3.Distance(headsetPosition, leftControllerPosition);
        // var rightDistance = Vector3.Distance(headsetPosition, rightControllerPosition);

        var leftRelativeCoordinate = headset.transform.InverseTransformPoint(leftControllerPosition);
        var rightRelativeCoordinate = headset.transform.InverseTransformPoint(rightControllerPosition);

        coordinateText.SetText("Headset world coordinates: " + headsetPosition + "\nLeft controller relative: " + leftRelativeCoordinate + "\nRight controller relative: " + rightRelativeCoordinate +
        "\n\nLeft controller rotation: " + leftController.transform.rotation.eulerAngles + "\nRight controller rotation: " + rightController.transform.rotation.eulerAngles);
    }
}
