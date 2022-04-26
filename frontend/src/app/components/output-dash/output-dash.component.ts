import { Component, OnInit } from '@angular/core';
import {RequestBody} from '../../models/request-body';

const request_title = "POST Request Body";
const response_title = "JSON Response Body";

@Component({
  selector: 'app-output-dash',
  templateUrl: './output-dash.component.html',
  styleUrls: ['./output-dash.component.css']
})
export class OutputDashComponent implements OnInit {
  title = request_title;
  request_bodies: RequestBody[] = [];
  json_string = '';
  constructor() { }

  make_json(): void {
    this.json_string = JSON.stringify(
      {
        "list":this.request_bodies
      }
    );
  }
  ngOnInit(): void {
  }

}
