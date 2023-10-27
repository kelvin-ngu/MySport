import { TestBed } from '@angular/core/testing';

import { PostgatheringService } from './postgathering.service';

describe('PostgatheringService', () => {
  let service: PostgatheringService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PostgatheringService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
