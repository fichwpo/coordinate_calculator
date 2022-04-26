import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OutputDashComponent } from './output-dash.component';

describe('OutputDashComponent', () => {
  let component: OutputDashComponent;
  let fixture: ComponentFixture<OutputDashComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OutputDashComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OutputDashComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
