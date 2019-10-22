import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BlogGetoneComponent } from './blog-getone.component';

describe('BlogGetoneComponent', () => {
  let component: BlogGetoneComponent;
  let fixture: ComponentFixture<BlogGetoneComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BlogGetoneComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BlogGetoneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
