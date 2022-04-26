import {Component, OnInit, ViewChild} from '@angular/core';
import {RequestBody} from './models/request-body';
import {OutputDashComponent} from './components/output-dash/output-dash.component';

const request_title = "POST Request Body";
const response_title = "JSON Response Body";
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {

  title = 'frontend';
  @ViewChild(OutputDashComponent) outputDash!: OutputDashComponent;
  constructor(){}
  ngOnInit(){
  }

  addRequest(req_body:RequestBody){
    this.outputDash.title = request_title;
    this.outputDash.request_bodies.push(req_body);
    this.outputDash.make_json();
  }

  async submit(){
    const payload = JSON.stringify({
      "list" : this.outputDash.request_bodies
    });
    this.outputDash.request_bodies = [];
    this.outputDash.title = response_title;

    const url = "http://127.0.0.1:5000/calculate";

    const myHeaders = new Headers();
    myHeaders.append("Body-Type", "list");
    myHeaders.append("Content-Type", "application/json");
    myHeaders.append("Origin", "http://localhost/4200")
    myHeaders.append("Access-Control-Allow-Origin", "http://127.0.0.1:5000/calculate");
    let requestOptions: RequestInit = {
      method: 'POST',
      headers: myHeaders,
      body: payload,
      redirect: "follow",
    };

    const response = await fetch(url, requestOptions)
    this.outputDash.json_string = await response.text();

  }

}
