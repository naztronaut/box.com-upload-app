import React, { Component } from "react";
import { FileUpload } from "primereact/fileupload";
import { ProgressBar } from "primereact/progressbar";
import { Growl } from "primereact/growl";

class BoxUpload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      progressStatus: false,
    };
  }

  onBeforeUpload = (e) => {
    console.log(e);
    this.setState({ progressStatus: true });
    this.growl.show({
      severity: "info",
      summary: "Upload Started",
      detail: "Uploading File to Box",
    });
  };

  onUpload = (data) => {
    console.log(data);
    this.setState({ progressStatus: false });
    this.growl.show({
      severity: "success",
      summary: "Upload Completed",
      detail: "File Successfully uploaded to Box",
    });
  };

  onError = (e) => {
    console.log(e);
    this.growl.show({
      severity: "error",
      summary: "Upload Failed",
      detail: "File Failed to upload. Check logs.",
    });
  };

  myUploader = (event) => {
    console.log(event);
    console.log(this);
  };

  render() {
    return (
      <React.Fragment>
        {
          <Growl
            ref={(el) => {
              this.growl = el;
            }}
          ></Growl>
        }
        {this.state.progressStatus && (
          <ProgressBar
            mode="indeterminate"
            style={{ height: "6px" }}
          ></ProgressBar>
        )}
        <FileUpload
          name="uploaded"
          mode="basic"
          url="/upload"
          onBeforeUpload={this.onBeforeUpload}
          onUpload={this.onUpload}
          onError={this.onError}
          multiple={false}
          // accept="image/*"
          // maxFileSize={1000000}
          // customUpload={true}
          // uploadHandler={this.myUploader}
        />
      </React.Fragment>
    );
  }
}

export default BoxUpload;
